import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Define dataset paths
DATASET_PATH = r'd:\ emotions_dataset'
TRAIN_PATH = os.path.join(DATASET_PATH, 'dataset', 'train')
TEST_PATH = os.path.join(DATASET_PATH, 'dataset', 'test')
STATIC_PATH = os.path.join(DATASET_PATH, 'static', 'images')

# Create static directory if it doesn't exist
os.makedirs(STATIC_PATH, exist_ok=True)

def count_images_per_category(base_path, emotion_categories):
    """Count images in each emotion category"""
    counts = {}
    for emotion in emotion_categories:
        emotion_path = os.path.join(base_path, emotion)
        if os.path.exists(emotion_path):
            counts[emotion] = len([f for f in os.listdir(emotion_path) if f.endswith('.jpg')])
    return counts

def load_sample_images(emotion_categories):
    """Load sample images from each category"""
    sample_images = {}
    for emotion in emotion_categories:
        emotion_path = os.path.join(TRAIN_PATH, emotion)
        if os.path.exists(emotion_path):
            files = [f for f in os.listdir(emotion_path) if f.endswith('.jpg')]
            if files:
                sample_path = os.path.join(emotion_path, files[0])
                img = cv2.imread(sample_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                sample_images[emotion] = img
    return sample_images

def analyze_image_stats(base_path, emotion_categories):
    """Analyze image statistics"""
    stats = {'widths': [], 'heights': [], 'channels': [], 'file_sizes': []}
    
    for emotion in emotion_categories:
        emotion_path = os.path.join(base_path, emotion)
        if os.path.exists(emotion_path):
            for filename in os.listdir(emotion_path):
                if filename.endswith('.jpg'):
                    img_path = os.path.join(emotion_path, filename)
                    try:
                        img = cv2.imread(img_path)
                        h, w, c = img.shape
                        stats['heights'].append(h)
                        stats['widths'].append(w)
                        stats['channels'].append(c)
                        stats['file_sizes'].append(os.path.getsize(img_path))
                    except Exception as e:
                        print(f"Error analyzing {img_path}: {e}")
    
    return stats

def generate_all_graphs():
    """Generate and save all visualization graphs"""
    
    # Get emotion categories
    emotion_categories = os.listdir(TRAIN_PATH)
    print(f"Generating graphs for emotions: {emotion_categories}")
    
    # Count images
    train_counts = count_images_per_category(TRAIN_PATH, emotion_categories)
    test_counts = count_images_per_category(TEST_PATH, emotion_categories)
    
    # 1. Distribution Bar Charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    emotions = list(train_counts.keys())
    train_values = list(train_counts.values())
    test_values = list(test_counts.values())
    
    ax1.bar(emotions, train_values, color='skyblue', alpha=0.8)
    ax1.set_title('Training Set Distribution', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Emotion Categories')
    ax1.set_ylabel('Number of Images')
    ax1.tick_params(axis='x', rotation=45)
    
    ax2.bar(emotions, test_values, color='lightcoral', alpha=0.8)
    ax2.set_title('Test Set Distribution', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Emotion Categories')
    ax2.set_ylabel('Number of Images')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig(os.path.join(STATIC_PATH, 'distribution_bars.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Pie Chart
    total_counts = {emotion: train_counts[emotion] + test_counts[emotion] for emotion in emotions}
    
    plt.figure(figsize=(10, 8))
    colors = plt.cm.Set3(np.linspace(0, 1, len(emotions)))
    wedges, texts, autotexts = plt.pie(total_counts.values(), labels=total_counts.keys(), 
                                       autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Overall Dataset Distribution by Emotion', fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.savefig(os.path.join(STATIC_PATH, 'distribution_pie.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Sample Images Grid
    sample_images = load_sample_images(emotion_categories)
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()
    
    for idx, (emotion, img) in enumerate(sample_images.items()):
        if idx < len(axes):
            axes[idx].imshow(img)
            axes[idx].set_title(f'{emotion.capitalize()}', fontsize=12, fontweight='bold')
            axes[idx].axis('off')
    
    # Hide unused subplots
    for idx in range(len(sample_images), len(axes)):
        axes[idx].axis('off')
    
    plt.suptitle('Sample Images from Each Emotion Category', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(STATIC_PATH, 'sample_images.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Image Statistics
    train_stats = analyze_image_stats(TRAIN_PATH, emotion_categories)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Width distribution
    ax1.hist(train_stats['widths'], bins=20, alpha=0.7, color='blue')
    ax1.set_title('Image Width Distribution')
    ax1.set_xlabel('Width (pixels)')
    ax1.set_ylabel('Frequency')
    
    # Height distribution
    ax2.hist(train_stats['heights'], bins=20, alpha=0.7, color='green')
    ax2.set_title('Image Height Distribution')
    ax2.set_xlabel('Height (pixels)')
    ax2.set_ylabel('Frequency')
    
    # File size distribution
    file_sizes_kb = [size/1024 for size in train_stats['file_sizes']]
    ax3.hist(file_sizes_kb, bins=20, alpha=0.7, color='red')
    ax3.set_title('File Size Distribution')
    ax3.set_xlabel('File Size (KB)')
    ax3.set_ylabel('Frequency')
    
    # Aspect ratio distribution
    aspect_ratios = [w/h for w, h in zip(train_stats['widths'], train_stats['heights'])]
    ax4.hist(aspect_ratios, bins=20, alpha=0.7, color='orange')
    ax4.set_title('Aspect Ratio Distribution')
    ax4.set_xlabel('Aspect Ratio (W/H)')
    ax4.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig(os.path.join(STATIC_PATH, 'image_statistics.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 5. Dataset Summary Table as Image
    summary_data = {
        'Emotion': emotion_categories,
        'Training Images': [train_counts[emotion] for emotion in emotion_categories],
        'Test Images': [test_counts[emotion] for emotion in emotion_categories],
        'Total Images': [train_counts[emotion] + test_counts[emotion] for emotion in emotion_categories]
    }
    
    summary_df = pd.DataFrame(summary_data)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('tight')
    ax.axis('off')
    
    table = ax.table(cellText=summary_df.values, colLabels=summary_df.columns,
                     cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.5)
    
    # Style the table
    for i in range(len(summary_df.columns)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    plt.title('Dataset Summary', fontsize=16, fontweight='bold', pad=20)
    plt.savefig(os.path.join(STATIC_PATH, 'dataset_summary.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print("All graphs generated successfully!")
    print(f"Graphs saved to: {STATIC_PATH}")
    
    return {
        'total_images': sum(summary_df['Total Images']),
        'num_categories': len(emotion_categories),
        'categories': emotion_categories,
        'train_total': sum(train_counts.values()),
        'test_total': sum(test_counts.values())
    }

if __name__ == "__main__":
    stats = generate_all_graphs()
    print(f"Dataset Statistics: {stats}")
