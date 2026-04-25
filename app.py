from flask import Flask, render_template, jsonify
import os
from generate_graphs import generate_all_graphs

app = Flask(__name__)

# Configure static folder
app.static_folder = 'static'

@app.route('/')
def landing_page():
    """Main landing page showing all emotion dataset visualizations"""
    
    # Generate fresh graphs
    try:
        stats = generate_all_graphs()
        
        # Define the graphs to display
        graphs = [
            {
                'title': 'Dataset Distribution',
                'description': 'Training and test set distribution across emotion categories',
                'image': 'images/distribution_bars.png',
                'type': 'bar'
            },
            {
                'title': 'Overall Distribution',
                'description': 'Pie chart showing balanced distribution of emotions',
                'image': 'images/distribution_pie.png',
                'type': 'pie'
            },
            {
                'title': 'Sample Images',
                'description': 'Representative images from each emotion category',
                'image': 'images/sample_images.png',
                'type': 'grid'
            },
            {
                'title': 'Image Statistics',
                'description': 'Analysis of image dimensions, file sizes, and aspect ratios',
                'image': 'images/image_statistics.png',
                'type': 'histogram'
            },
            {
                'title': 'Dataset Summary',
                'description': 'Complete overview of dataset composition',
                'image': 'images/dataset_summary.png',
                'type': 'table'
            }
        ]
        
        return render_template('landing.html', 
                             graphs=graphs, 
                             stats=stats,
                             success=True)
    
    except Exception as e:
        return render_template('landing.html', 
                             graphs=[], 
                             stats={},
                             success=False,
                             error=str(e))

@app.route('/api/stats')
def get_stats():
    """API endpoint to get dataset statistics"""
    try:
        stats = generate_all_graphs()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/regenerate')
def regenerate_graphs():
    """Regenerate all graphs and redirect to landing page"""
    try:
        generate_all_graphs()
        return jsonify({'success': True, 'message': 'Graphs regenerated successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static/images', exist_ok=True)
    
    print("Starting Emotions Dataset Visualization Server...")
    print("Access the landing page at: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
