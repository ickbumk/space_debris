# Space Debris Characterization and Attitude Estimation via YOLO and Kalman Filtering

Kalman filtering and YOLO for space debris characterization and attitude estimation.

## Instructions for cloning and creating a branch

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ickbumk/space_debris.git
cd space_debris
```

### 2. Create a new branch

Do not make changes directly on the `main` branch. Create a new branch for your work:

```bash
git checkout -b <your-branch-name>
```

For example:

```bash
git checkout -b feature/yolo-detection
```

You can verify which branch you are currently on with:

```bash
git branch
```

The branch with the `*` is your current branch.

### 3. Make your changes

Make your code changes in your local copy of the repository.

For example:

```text
space_debris/
├── ...
├── your_new_code.py
└── README.md
```

You can check which files have changed with:

```bash
git status
```

### 4. Commit your changes

After you are satisfied with your changes, stage them:

```bash
git add .
```

Then create a commit:

```bash
git commit -m "Describe your changes"
```

For example:

```bash
git commit -m "Add YOLO debris detection"
```

### 5. Push your branch

Push your branch to GitHub:

```bash
git push -u origin <your-branch-name>
```

For example:

```bash
git push -u origin feature/yolo-detection
```

The `-u` option connects your local branch to the corresponding remote branch. After the first push, you can simply use:

```bash
git push
```

---

## Creating a Merge Request

Once your work has been pushed, create a **Pull Request (PR)** on GitHub.

1. Go to the repository on GitHub.
2. GitHub should show that your branch was recently pushed.
3. Select **Compare & pull request**.
4. Set the target/base branch to:

```text
main
```

5. Set the source/compare branch to your feature branch:

```text
feature/yolo-detection
```

6. Add a descriptive title and explain what you changed.
7. Create the Pull Request.

### Pull Request description

Please include:

* What you changed
* Why the change was needed
* How the code was tested
* Any dependencies or setup changes
* Any known issues or limitations

For example:

```text
## Changes

- Added YOLO-based space debris detection.
- Added bounding-box extraction.
- Added initial Kalman filter tracking.

## Testing

- Tested on the provided debris image dataset.
- Verified detection and tracking over consecutive frames.

## Notes

- Additional tuning of the Kalman filter may be required.
```

---

## Code Review and Merging

After you create the Pull Request, **do not merge it yourself**.

I will review the changes and provide comments or requested modifications.

The workflow is:

```text
Create branch
     ↓
Make changes
     ↓
Commit changes
     ↓
Push branch
     ↓
Open Pull Request
     ↓
Code review
     ↓
Address review comments
     ↓
Approval
     ↓
Merge into main
```

If changes are requested during the review, make the changes on the same branch:

```bash
git checkout <your-branch-name>
```

Edit the code, then:

```bash
git add .
git commit -m "Address review comments"
git push
```

The Pull Request will automatically update with the new commit.

Once the changes have been reviewed and approved, the Pull Request will be merged into `main`.

---

## Keeping Your Branch Up to Date

Before starting new work, update your local `main` branch:

```bash
git checkout main
git pull origin main
```

Then create a new feature branch:

```bash
git checkout -b <new-branch-name>
```

For example:

```bash
git checkout main
git pull origin main
git checkout -b feature/kalman-filter
```

This keeps new work based on the latest version of `main`.

## Recommended Branch Naming

Use descriptive branch names based on the work being done:

```text
feature/yolo-detection
feature/kalman-filter
feature/attitude-estimation
feature/data-generation
feature/preprocessing
fix/detection-bug
fix/tracking-bug
docs/update-readme
```

Avoid generic branch names such as:

```text
test
new
stuff
mybranch
changes
```

## Important

* Do **not** commit directly to `main`.
* Create a separate branch for each feature or bug fix.
* Keep commits focused and descriptive.
* Push your branch and create a Pull Request when the work is ready for review.
* The `main` branch should contain reviewed and working code.
* Do not force-push to `main`.
* If a review requires changes, update the same Pull Request rather than creating a new one.
