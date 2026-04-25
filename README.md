# Emotions Dataset Visualization Dashboard

A comprehensive Flask web application that provides preprocessing analysis and visualization of facial emotion recognition datasets. This project combines data preprocessing, statistical analysis, and interactive web visualization in one complete package.

## Dataset Overview

This project works with facial emotion recognition datasets containing 8 emotion categories:
- **Angry** - Facial expressions showing anger
- **Contempt** - Expressions of contempt/disdain
- **Disgust** - Disgusted facial expressions
- **Fear** - Fearful expressions
- **Happy** - Happy/joyful expressions
- **Neutral** - Neutral facial expressions
- **Sad** - Sad/sorrowful expressions
- **Surprised** - Surprised facial expressions

### Dataset Statistics
- **Total Images**: 152 images
- **Training Set**: 112 images (14 per emotion)
- **Test Set**: 40 images (5 per emotion)
- **Image Format**: JPG files
- **Balanced Distribution**: Equal samples per emotion category

## Preprocessing Pipeline

### 1. Data Loading and Structure Analysis
- **Directory Scanning**: Automatic detection of emotion categories
- **Image Counting**: Statistical analysis of dataset distribution
- **Path Validation**: Ensures correct dataset structure
- **Error Handling**: Graceful handling of missing or corrupted files

### 2. Image Preprocessing
- **Resizing**: Standardized to 224x224 pixels for model compatibility
- **Color Space Conversion**: BGR to RGB conversion for proper display
- **Normalization**: Pixel values normalized to [0, 1] range
- **Data Type Conversion**: Float32 format for efficient processing

### 3. Label Encoding
- **String to Numeric**: Emotion names converted to numeric labels
- **Consistent Mapping**: Maintains same encoding across train/test sets
- **Reversible Encoding**: Can decode back to emotion names

### 4. Data Augmentation (Preview)
- **Rotation**: ±20 degrees random rotation
- **Translation**: 20% width/height shift
- **Horizontal Flip**: Random horizontal flipping
- **Zoom**: 20% random zoom in/out
- **Shear**: 20% shear transformation
- **Fill Mode**: Nearest pixel fill for transformed areas

### 5. Statistical Analysis
- **Image Dimensions**: Width/height distribution analysis
- **File Size Analysis**: Storage requirements assessment
- **Aspect Ratio**: Image proportion analysis
- **Quality Metrics**: Consistency and quality evaluation

## Flask Web Application Features

### Dashboard Components
- **Interactive Dashboard**: Beautiful landing page with all dataset visualizations
- **Real-time Graph Generation**: Automatically generates and displays:
  - Dataset distribution bar charts
  - Pie chart showing emotion balance
  - Sample images from each category
  - Image statistics (dimensions, file sizes, aspect ratios)
  - Dataset summary table
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Bootstrap 5 with custom CSS and animations




## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask App**:
   ```bash
   python app.py
   ```

3. **Open Browser**:
   Navigate to `http://localhost:5000`

## Project Structure

```
emotions_dataset/
├── dataset/
│   ├── train/          # Training images by emotion
│   └── test/           # Test images by emotion
├── static/
│   └── images/         # Generated graph images
├── templates/
│   └── landing.html    # Main dashboard template
├── app.py              # Flask application
├── generate_graphs.py  # Graph generation script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dataset Structure Expected

```
dataset/
├── train/
│   ├── angry/
│   ├── contempt/
│   ├── disgust/
│   ├── fear/
│   ├── happy/
│   ├── neutral/
│   ├── sad/
│   └── surprised/
└── test/
    ├── angry/
    ├── contempt/
    ├── disgust/
    ├── fear/
    ├── happy/
    ├── neutral/
    ├── sad/
    └── surprised/
```


## Flask Application Architecture

### Backend Structure
```
app.py                 # Main Flask application
├── Routes:
│   ├── / (GET)        # Landing page with visualizations
│   ├── /api/stats     # JSON API for dataset statistics
│   └── /regenerate    # Regenerate graphs endpoint
├── Functions:
│   ├── landing_page() # Main dashboard route
│   ├── get_stats()    # Statistics API endpoint
│   └── regenerate_graphs() # Graph regeneration
```

### Frontend Components
```
templates/landing.html  # Main dashboard template
├── Hero Section       # Title and overview
├── Statistics Cards   # Key metrics display
├── Graph Gallery      # Interactive visualizations
├── Error Handling     # Graceful error display
└── Responsive Design  # Mobile-friendly layout
```

### Static Assets
```
static/images/         # Generated visualization images
├── distribution_bars.png    # Train/test distribution
├── distribution_pie.png     # Overall emotion balance
├── sample_images.png        # Representative samples
├── image_statistics.png     # Dimension analysis
└── dataset_summary.png      # Summary table
```

## Visualization Details

### 1. Distribution Analysis
- **Bar Charts**: Side-by-side comparison of training vs test sets
- **Pie Chart**: Proportional representation of each emotion
- **Color Coding**: Consistent color scheme across visualizations
- **Interactive Elements**: Hover effects and responsive design

### 2. Sample Image Gallery
- **Grid Layout**: 2x4 grid showing one sample per emotion
- **Image Processing**: Proper color space conversion and display
- **Labeling**: Clear emotion category labels
- **Quality**: High-resolution display with proper scaling

### 3. Statistical Histograms
- **Width Distribution**: Pixel width analysis across all images
- **Height Distribution**: Pixel height analysis
- **File Size Analysis**: Storage requirements in KB
- **Aspect Ratio**: Width-to-height ratio distribution

### 4. Dataset Summary Table
- **Comprehensive Overview**: All metrics in tabular format
- **Color Coding**: Professional styling with headers
- **Export Ready**: Clean format suitable for reports
- **Dynamic Generation**: Updates automatically with data changes

## Preprocessing Workflow

### Step-by-Step Process
1. **Initialize Paths**: Set up dataset directory structure
2. **Scan Directories**: Detect emotion categories automatically
3. **Count Images**: Generate distribution statistics
4. **Load Samples**: Read representative images from each category
5. **Analyze Properties**: Extract image dimensions and file sizes
6. **Generate Visualizations**: Create all graphs and charts
7. **Save Assets**: Store images in static directory
8. **Serve Dashboard**: Display results in web interface

### Data Validation
- **Path Verification**: Ensures correct directory structure
- **File Format Check**: Validates JPG image files
- **Corruption Detection**: Handles damaged or unreadable files
- **Consistency Validation**: Verifies balanced dataset distribution

## Customization Options

### Graph Styling
```python
# Modify in generate_graphs.py
plt.style.use('seaborn-v0_8')  # Change plot style
sns.set_palette("husl")        # Modify color palette
colors = plt.cm.Set3(...)      # Custom color schemes
```

### Image Processing Parameters
```python
# Adjust in preprocessing functions
target_size = (224, 224)      # Change image dimensions
normalize = True              # Toggle normalization
data_type = 'float32'         # Modify data type
```

### Flask Configuration
```python
# Customize in app.py
app.run(debug=True,           # Development mode
        host='0.0.0.0',       # Network accessibility
        port=5000)            # Port configuration
```

## Troubleshooting Guide

### Common Issues
1. **Path Errors**: Verify dataset directory structure matches expected format
2. **Missing Images**: Ensure all emotion folders contain JPG files
3. **Import Errors**: Install all dependencies from requirements.txt
4. **Port Conflicts**: Change Flask port if 5000 is occupied
5. **Permission Issues**: Check file/directory read permissions

### Debug Mode
```bash
# Run with debug information
python app.py
# Flask will show detailed error messages
```

### Validation Commands
```bash
# Check dataset structure
python -c "import os; print(os.listdir('dataset/train'))"

# Verify dependencies
pip list | grep -E "(Flask|matplotlib|opencv)"

# Test graph generation
python generate_graphs.py
```

