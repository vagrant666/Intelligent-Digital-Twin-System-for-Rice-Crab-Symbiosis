# Contribution Guide
## Branch Rule
1. main: stable release branch, only merged after full test
2. dev: development branch for new features
3. feature-xxx: single function development branch

## Code Standard
1. All python files must contain detailed Chinese/English comments
2. Strict modular split, no repeated code
3. Variable & function name use snake_case
4. Data interface only support official real API, forbidden simulation data

## Pull Request Process
1. Fork this repository
2. Create feature branch from dev
3. Complete unit test in tests/unit_test.py
4. Submit PR with function description, test result screenshot
5. Pass code review before merge

## Issue Submit
If you meet API access error, training loss abnormal, visualization failure:
1. Attach complete log in logs/system_run.log
2. Record operating system, python & torch version
3. Describe reproduce steps clearly
'@ | Out-File CONTRIBUTING.md -Encoding utf8