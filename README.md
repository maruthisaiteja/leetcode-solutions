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

### 2026-05-29

| Problem | Difficulty | Status | Runtime | Language | Code |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Minimum Element After Replacement With Digit Sum](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/) | Easy | Accepted | 3 ms | python3 | [solution](./solutions/2026-05-29/minimum-element-after-replacement-with-digit-sum.py) |
| [Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) | Easy | Accepted | 0 ms | python3 | [solution](./solutions/2026-05-29/maximum-score-after-splitting-a-string.py) |
| [Check If All 1's Are at Least Length K Places Away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/) | Easy | Accepted | 9 ms | python3 | [solution](./solutions/2026-05-29/check-if-all-1s-are-at-least-length-k-places-away.py) |
| [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | Medium | Accepted | 480 ms | python3 | [solution](./solutions/2026-05-29/max-number-of-k-sum-pairs.py) |
| [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/) | Hard | Accepted | 47 ms | python3 | [solution](./solutions/2026-05-29/find-in-mountain-array.py) |
| [Escape a Large Maze](https://leetcode.com/problems/escape-a-large-maze/) | Hard | Accepted | 1316 ms | python3 | [solution](./solutions/2026-05-29/escape-a-large-maze.py) |
