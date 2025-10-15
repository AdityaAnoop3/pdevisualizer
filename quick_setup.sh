#!/bin/bash
# Quick setup script for PDEVisualizer production packaging

set -e
echo "🚀 Setting up PDEVisualizer for production..."
echo ""

# Create directory structure
echo "✓ Creating directories..."
mkdir -p .github/workflows
mkdir -p docs/_static docs/_templates docs/api docs/tutorials docs/examples
mkdir -p notebooks/examples

# Create placeholder files
echo "✓ Creating configuration files..."

# Only create if they don't exist
[ ! -f "MANIFEST.in" ] && touch MANIFEST.in
[ ! -f "CHANGELOG.md" ] && touch CHANGELOG.md
[ ! -f ".readthedocs.yaml" ] && touch .readthedocs.yaml
[ ! -f "DEPLOYMENT_GUIDE.md" ] && touch DEPLOYMENT_GUIDE.md
[ ! -f "docs/Makefile" ] && touch docs/Makefile
[ ! -f "docs/conf.py" ] && touch docs/conf.py
[ ! -f "docs/index.rst" ] && touch docs/index.rst
[ ! -f ".github/workflows/ci.yml" ] && touch .github/workflows/ci.yml
[ ! -f ".github/workflows/publish.yml" ] && touch .github/workflows/publish.yml

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
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

# Virtual environments
venv/
ENV/
env/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Documentation
docs/_build/
docs/auto_examples/
docs/generated/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Generated outputs
*.gif
*.mp4
*.png
!docs/_static/*.png

# Jupyter
.ipynb_checkpoints/
EOF
fi

echo ""
echo "✅ Directory structure created!"
echo ""
echo "📁 Project structure:"
tree -L 2 -I '__pycache__|*.pyc|*.egg-info' . || ls -R

echo ""
echo "Next: Show me the output of these commands:"
echo "  1. ls -la src/pdevisualizer/"
echo "  2. cat pyproject.toml"
echo ""
echo "Then I'll populate all the configuration files!"
