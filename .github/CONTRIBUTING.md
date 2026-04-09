# Contributing to Healthcare Backend

First off, thanks for taking the time to contribute! 🎉

## Code of Conduct
This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs
Before creating bug reports, please check if the issue already exists. When you create a bug report, include as many details as possible:
- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include screenshots if possible

### Suggesting Enhancements
Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:
- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Explain why this enhancement would be useful

### Pull Requests
- Assign yourself to the PR
- Link any related issues
- Keep PRs focused on a single feature or fix
- Write clear commit messages
- Add tests for new features
- Update documentation as needed

## Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Docker & Docker Compose (optional but recommended)

### Local Setup
```bash
# Clone the repository
git clone https://github.com/your-username/healthcare_backend.git
cd healthcare_backend

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Running Tests
```bash
# Run all tests
python manage.py test tests/

# Run specific test file
python manage.py test tests.test_auth

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test tests/
coverage report
```

### Code Style
- Follow PEP 8
- Use 4 spaces for indentation
- Keep lines under 100 characters where possible
- Write meaningful variable and function names

### Commit Messages
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Documentation
- Update README.md for user-facing changes
- Add docstrings to functions and classes
- Update API documentation in comments
- Keep docs in sync with code changes

## Project Structure

```
healthcare_backend/
├── accounts/          # User authentication and authorization
├── patients/          # Patient management APIs
├── doctors/           # Doctor management APIs
├── mappings/          # Patient-Doctor relationship management
├── config/            # Django configuration
├── tests/             # Test suite
└── healthcare_backend/ # Main Django project
```

## Branching Strategy
- `main` - Production-ready code
- `develop` - Development branch
- Feature branches: `feature/your-feature-name`
- Bug fixes: `bugfix/your-bug-name`

### Creating a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### Before Submitting a Pull Request
1. Update the documentation
2. Add or update tests
3. Run the test suite: `python manage.py test tests/`
4. Make sure your code follows the style guide
5. Ensure your commit messages are clear

## Additional Notes

### Issue and Pull Request Labels
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

### Getting Help
- Check existing issues and discussions
- Ask on GitHub Discussions
- Join our community chat (if available)

## License
By contributing, you agree that your contributions will be licensed under the same license as the project.

Thank you for contributing! 🚀
