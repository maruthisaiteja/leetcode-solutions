# LeetCode GitHub Agent

An autonomous agent system built in Node.js that fetches LeetCode problems (the daily challenge + random unsolved problems), solves them using the Gemini 2.5 Flash API in Python, submits them directly to LeetCode, and commits accepted solutions to GitHub.

---

## Setup Instructions

### 1. Environment Variables Setup

Copy `.env.example` to a new file named `.env`:
```bash
cp .env.example .env
```
Fill in the values for each key in `.env`.

---

### 2. Retrieving LeetCode Credentials

To submit solutions automatically, the agent requires your active LeetCode session cookies (`LEETCODE_SESSION` and `LEETCODE_CSRF`).

1. Open your browser and go to [LeetCode](https://leetcode.com/).
2. Log in to your account.
3. Open the **Developer Tools** (Press `F12` or Right-click and choose **Inspect**).
4. Navigate to the **Application** tab (Chrome/Edge) or **Storage** tab (Firefox).
5. Under the **Cookies** section in the left sidebar, click on `https://leetcode.com`.
6. Search for the following keys and copy their **Value**:
   - `LEETCODE_SESSION`: A long alphanumeric string.
   - `csrftoken`: Copy this value and paste it as `LEETCODE_CSRF` in your `.env` file.

---

### 3. Retrieving GitHub Credentials

The agent automatically commits your accepted solutions and updates your daily progress log on GitHub.

1. Go to your GitHub account settings -> **Developer Settings** -> **Personal Access Tokens** -> **Fine-grained tokens** (or **Tokens (classic)**).
2. Click **Generate new token**.
3. Grant the token `repo` scopes (or write access to code/contents if using fine-grained tokens).
4. Copy the generated token and paste it as `GITHUB_TOKEN` in your `.env` file.
5. Create a GitHub repository named `leetcode-solutions` (or whatever you set `GITHUB_REPO` to) under your account.

---

### 4. Running the System

#### Running a Dry Run (Recommended for testing)
To dry-run the agents, which queries LeetCode and Gemini but skips actual submissions and commits:
```bash
npm run run -- --dry-run
```

#### Running the System Immediately
To run the solving process once immediately:
```bash
npm run run -- --now
```

#### Starting the Cron Scheduler (Production Daemon)
To start the daemon that schedules runs daily at 7:00 AM IST (1:30 AM UTC):
```bash
npm start
```

---

## GitHub Actions Cloud Setup

To run this workflow automatically every day in the cloud:

1. Create a private repository on GitHub (e.g., `leetcode-github-agent`).
2. Go to **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**.
3. Add the following secrets:
   - `GEMINI_API_KEY`: Your Gemini API key.
   - `LEETCODE_SESSION`: Your LeetCode session cookie.
   - `LEETCODE_CSRF`: Your LeetCode CSRF token.
   - `GH_USERNAME`: Your GitHub username (optional; defaults to the repository owner).
4. Push this repository to GitHub. The workflow in `.github/workflows/daily.yml` will run automatically every day at 01:30 UTC, and can be manually triggered via the Actions tab.

---

## Daily Log

### 2026-05-23

| Problem | Difficulty | Status | Runtime | Language | Code |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) | Easy | Accepted | 0 ms | python3 | [solution](./solutions/2026-05-23/check-if-array-is-sorted-and-rotated.py) |
| [Water Bottles](https://leetcode.com/problems/water-bottles/) | Easy | Accepted | 0 ms | python3 | [solution](./solutions/2026-05-23/water-bottles.py) |
| [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/) | Easy | Accepted | 0 ms | python3 | [solution](./solutions/2026-05-23/xor-operation-in-an-array.py) |
| [Array Nesting](https://leetcode.com/problems/array-nesting/) | Medium | Accepted | 50 ms | python3 | [solution](./solutions/2026-05-23/array-nesting.py) |
| [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Medium | Accepted | 48 ms | python3 | [solution](./solutions/2026-05-23/continuous-subarray-sum.py) |
| [Form Largest Integer With Digits That Add up to Target](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) | Hard | Accepted | 375 ms | python3 | [solution](./solutions/2026-05-23/form-largest-integer-with-digits-that-add-up-to-target.py) |
| [Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) | Hard | Accepted | 87 ms | python3 | [solution](./solutions/2026-05-23/number-of-ways-to-stay-in-the-same-place-after-some-steps.py) |

### 2026-05-28

| Problem | Difficulty | Status | Runtime | Language | Code |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Longest Common Suffix Queries](https://leetcode.com/problems/longest-common-suffix-queries/) | Hard | Accepted | 2381 ms | python3 | [solution](./solutions/2026-05-28/longest-common-suffix-queries.py) |
| [Projection Area of 3D Shapes](https://leetcode.com/problems/projection-area-of-3d-shapes/) | Easy | Accepted | 3 ms | python3 | [solution](./solutions/2026-05-28/projection-area-of-3d-shapes.py) |
| [DI String Match](https://leetcode.com/problems/di-string-match/) | Easy | Accepted | 3 ms | python3 | [solution](./solutions/2026-05-28/di-string-match.py) |
| [Earliest Finish Time for Land and Water Rides II](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/) | Medium | Accepted | 675 ms | python3 | [solution](./solutions/2026-05-28/earliest-finish-time-for-land-and-water-rides-ii.py) |
| [Count of Integers](https://leetcode.com/problems/count-of-integers/) | Hard | Accepted | 275 ms | python3 | [solution](./solutions/2026-05-28/count-of-integers.py) |
| [Split the Array to Make Coprime Products](https://leetcode.com/problems/split-the-array-to-make-coprime-products/) | Hard | Accepted | 231 ms | python3 | [solution](./solutions/2026-05-28/split-the-array-to-make-coprime-products.py) |
