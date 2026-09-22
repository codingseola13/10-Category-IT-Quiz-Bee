# IT Quiz Bee Trainer

A browser-based study app for IT Quiz Bee preparation. It combines structured lessons, a visual knowledge map, adaptive practice, typed recall, spaced repetition, mistake tracking, analytics, and timed competition simulation.

## Features

- Knowledge map covering 10 IT subject categories
- Learn and Review concept library
- Daily Review with spaced repetition
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

## Data and privacy

Progress is always stored in the browser using local storage. A user can optionally request a passwordless email sign-in link. When signed in, quiz history, mastery evidence, mistakes, and studied concepts are saved in Supabase and can be loaded on another device by signing in with the same email address.

The Supabase table and row-level security policies are documented in `supabase-setup.sql`. Each signed-in user can read and change only the row tied to their own authenticated user ID.

## Disclaimer

The question bank is practice material based on common IT concepts and the app's 10 scope categories. It is not an official UMak question set.
