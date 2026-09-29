# IT Quiz Bee Trainer

A browser-based study app for IT Quiz Bee preparation. It combines structured lessons, a visual knowledge map, adaptive practice, typed recall, spaced repetition, mistake tracking, analytics, and timed competition simulation.

## Features

- Knowledge map covering 10 IT subject categories
- Mobile-friendly compact Knowledge Map view
- Learn and Review concept library
- Daily Review with spaced repetition
- Free Voice Practice using browser speech recognition and read-aloud, with microphone checks, brief-silence retry, and specific recovery messages
- Recall scoring that accepts capitalization differences and equivalent terms, while flagging minor typos for review without awarding points
- Confidence tracking for guesses and uncertain answers
- Automatic Mistake Notebook with follow-up practice
- Adaptive 20-question Smart Drills
- 100-item timed elimination round
- Three-level identification final round
- Competition simulation
- Local progress and mastery tracking
- Optional email sign-in and Supabase cloud sync across devices
- Responsive dark and light modes

## Run locally

Download or clone the repository, then open `index.html` in a modern browser. No installation or account is required. Cloud sync is optional.

For spoken answers, open the hosted HTTPS site in Chrome or Edge and allow microphone access when asked. Embedded browsers may expose a speech-recognition button without providing the speech service; the app detects this case and keeps typed answers available.

## Data and privacy

Progress is always stored in the browser using local storage. A user can optionally request a passwordless email sign-in link. When signed in, quiz history, mastery evidence, mistakes, and studied concepts are saved in Supabase and can be loaded on another device by signing in with the same email address.

The Supabase table and row-level security policies are documented in `supabase-setup.sql`. Each signed-in user can read and change only the row tied to their own authenticated user ID.

## Disclaimer

The question bank is practice material based on common IT concepts and the app's 10 scope categories. It is not an official UMak question set.

## Question wording and answer checking

The short recall prompts in `question_copy.js` are aligned with the 130 explanations in Learn & Review. Every study-ready label now names one answer term, such as `Flow control`, while related terms such as congestion control are explained separately. Multiple-choice practice mixes those prompts with 100 reviewed core questions. The Final Round keeps three distinct levels: direct recall, short scenarios, and application or comparison. Question screens show the category without displaying the concept name before the learner answers.

Typed answers ignore capitalization and minor spacing differences. Correct expanded names and equivalent terms are accepted and displayed with standard capitalization, such as `PaaS — Platform as a Service`. A small spelling error is labeled **Close** but earns no point. Feedback begins with **Exact**, **Equivalent**, **Close**, or **Different**, followed by a one-sentence reason and an expandable explanation with a reference link.

Run the question-bank checks with:

```text
node validate_questions.js
```

The validator checks all 260 active prompts: 100 core multiple-choice questions, 130 recall variants, and 30 tiered Final Round questions. It also checks coverage, single-term study labels, answer indices, option uniqueness, prompt length, accepted answers, and accidental answer leakage.

The question review uses primary references for definitions and for topics where wording matters:

- [AWS cloud service models](https://aws.amazon.com/what-is/iaas/) for IaaS, PaaS, and SaaS.
- [OpenStax logic](https://openstax.org/books/contemporary-mathematics/pages/2-5-equivalent-statements) for converse, inverse, and contrapositive.
- [Microsoft Learn virtual memory](https://learn.microsoft.com/en-us/windows/win32/memory/virtual-address-space-and-physical-storage) and [working set](https://learn.microsoft.com/en-us/windows/win32/procthread/process-working-set).
- [The official Scrum Guide](https://scrumguides.org/scrum-guide.html) for Sprints.
- [Microsoft Learn OOP](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism) for inheritance, overriding, and runtime polymorphism.
- [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) and [UDP RFC 768](https://www.rfc-editor.org/info/rfc768/) for transport behavior.
- [NIST least privilege](https://csrc.nist.gov/glossary/term/least_privilege) and [password guidance](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/).
- [PostgreSQL joins](https://www.postgresql.org/docs/current/tutorial-join.html) and [foreign keys](https://www.postgresql.org/docs/current/tutorial-fk.html).
- [scikit-learn precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html) and [recall](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html).
- [MDN HTML, CSS, and JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview), [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET), and [CORS](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CORS).
