const fs = require('fs');
const vm = require('vm');

const scriptHead = fs.readFileSync('script.js', 'utf8').split(/\r?\n/).slice(0, 8).join('\n');
const questionCopy = fs.readFileSync('question_copy.js', 'utf8');
const context = {};
vm.createContext(context);
vm.runInContext(`${scriptHead}\n${questionCopy}\n;globalThis.quizData={categories,concepts,studyNotes,eliminationQuestions,finalQuestions,clearRecallPrompts,clearPromptAnswers,clearBasePrompts,clearFinalPrompts,clearFinalAnswers,trustedReferences,promptAnswerFor,finalPromptFor,finalAnswersFor};`, context);

const data = context.quizData;
const failures = [];
const check = (condition, message) => { if (!condition) failures.push(message); };
const words = value => String(value).trim().split(/\s+/).filter(Boolean).length;
const clean = value => String(value).toLowerCase().replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim();

const ready = Object.entries(data.concepts).flatMap(([category, items]) => items.map(concept => ({ category, concept })));
check(ready.length === 130, `Expected 130 study-ready concepts; found ${ready.length}.`);
check(new Set(ready.map(item => item.concept)).size === ready.length, 'Concept names must be unique across categories.');
check(Object.keys(data.trustedReferences).length === data.categories.length, 'Every category needs a trusted reference library.');

for (const { category, concept } of ready) {
  const note = data.studyNotes[category]?.[concept];
  const prompt = data.clearRecallPrompts[concept];
  const answers = data.clearPromptAnswers[concept] || [concept];
  check(concept === 'AND' || !/\b(?:vs|and)\b|\/|,/.test(concept.toLowerCase()), `${concept}: study-ready labels must identify one answer term.`);
  check(Array.isArray(note) && note.length === 3, `${concept}: expected explanation, example, and memory line.`);
  check(Boolean(prompt), `${concept}: missing recall prompt.`);
  if (!prompt) continue;
  check(prompt.endsWith('?'), `${concept}: recall prompt should end with a question mark.`);
  check(words(prompt) <= 25, `${concept}: recall prompt is longer than 25 words.`);
  for (const answer of answers) {
    const normalized = clean(answer);
    if (normalized.length >= 4) check(!clean(prompt).includes(normalized), `${concept}: prompt reveals accepted answer "${answer}".`);
  }
}

check(data.eliminationQuestions.length === 100, `Expected 100 core multiple-choice questions; found ${data.eliminationQuestions.length}.`);
for (const [index, question] of data.eliminationQuestions.entries()) {
  const prompt = data.clearBasePrompts[question.concept] || question.question;
  check(prompt.endsWith('?'), `Core question ${index + 1}: prompt should end with a question mark.`);
  check(words(prompt) <= 28, `Core question ${index + 1}: prompt is longer than 28 words.`);
  check(Array.isArray(question.options) && question.options.length === 4, `Core question ${index + 1}: expected four options.`);
  check(Number.isInteger(question.answer) && question.answer >= 0 && question.answer < question.options.length, `Core question ${index + 1}: invalid answer index.`);
  check(new Set(question.options.map(value => String(value).trim().toLowerCase())).size === question.options.length, `Core question ${index + 1}: duplicate options.`);
}

let generatedRecallCount = 0;
for (const category of data.categories) {
  const list = data.concepts[category];
  list.forEach((concept, index) => {
    const peers = [1, 3, 5].map(offset => list[(index + offset) % list.length]).filter(value => value !== concept);
    const options = [data.promptAnswerFor(concept), ...peers.map(data.promptAnswerFor)].filter((value, optionIndex, all) => all.indexOf(value) === optionIndex);
    check(options.length === 4, `${concept}: generated recall question does not have four unique options.`);
    if (options.length === 4) generatedRecallCount += 1;
  });
}
check(generatedRecallCount === 130, `Expected 130 generated recall questions; found ${generatedRecallCount}.`);

let finalCount = 0;
for (const [level, questions] of Object.entries(data.finalQuestions)) {
  check(questions.length === 10, `${level}: expected 10 Final Round questions.`);
  for (const question of questions) {
    finalCount += 1;
    const prompt = data.finalPromptFor(level, question);
    const answers = data.finalAnswersFor(question);
    check(Boolean(data.clearFinalPrompts[level]?.[question.concept]), `${level}/${question.concept}: missing reviewed Final Round prompt.`);
    check(prompt.endsWith('?'), `${level}/${question.concept}: prompt should end with a question mark.`);
    check(words(prompt) <= 28, `${level}/${question.concept}: prompt is longer than 28 words.`);
    check(Array.isArray(answers) && answers.length > 0, `${level}/${question.concept}: missing accepted answers.`);
    for (const answer of answers) {
      const normalized = clean(answer);
      if (normalized.length >= 4) check(!clean(prompt).includes(normalized), `${level}/${question.concept}: prompt reveals accepted answer "${answer}".`);
    }
  }
}
check(finalCount === 30, `Expected 30 Final Round questions; found ${finalCount}.`);

if (failures.length) {
  console.error(`Question validation failed (${failures.length} issue${failures.length === 1 ? '' : 's'}):`);
  failures.forEach(message => console.error(`- ${message}`));
  process.exit(1);
}

console.log(`Validated 260 questions: 100 core MCQs, 130 recall variants, and 30 tiered Final Round prompts.`);
console.log('Coverage: 130/130 study-ready concepts have notes, prompts, answer rules, and category references.');
