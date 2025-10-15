#!/bin/bash
# Complete production setup for PDEVisualizer
# Run this script to set up all production files

set -e
echo "🚀 PDEVisualizer Production Setup"
echo "=================================="
echo ""

# Create directory structure
echo "✓ Creating directory structure..."
mkdir -p .github/workflows
mkdir -p docs/_static docs/_templates
mkdir -p docs/api docs/tutorials docs/examples

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    echo "✓ Creating .gitignore..."
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
coverage.xml

# Documentation
docs/_build/
docs/auto_examples/
docs/generated/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/

# Generated outputs (keep in .gitignore, don't commit to repo)
*.gif
*.mp4
*.png
!docs/_static/*.png
EOF
fi

echo "✓ Installing/upgrading build tools..."
pip install --upgrade pip setuptools wheel build twine

echo "✓ Installing package in development mode..."
pip install -e ".[dev,docs]"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Copy all the artifact files I created into your project"
echo "2. Review and commit the changes:"
echo "   git add ."
echo "   git commit -m 'Add production packaging and CI/CD'"
echo "   git push origin main"
echo ""
echo "3. Test locally:"
echo "   - Run tests: pytest -v"
echo "   - Build docs: cd docs && make html"
echo "   - Build package: python -m build"
echo ""
echo "4. When ready to publish:"
echo "   - Follow instructions in DEPLOYMENT_GUIDE.md"
echo "   - Or run: ./publish_to_pypi.sh"
echo ""