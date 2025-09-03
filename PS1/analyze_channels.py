import numpy as np
import cv2

from ps1 import *

def analyze_southafrica_channels():
    """Analyze the three color channels of southafricaflagface.png"""
    
    img = cv2.imread('southafricaflagface.png')
    
    if img is None:
        print("Error: Could not load southafricaflagface.png")
        return
    
    print(f"Image shape: {img.shape}")
    print(f"Image dtype: {img.dtype}")
    
    # Extract the three channels (BGR in OpenCV)
    blue_channel = extract_blue(img)
    green_channel = extract_green(img)
    red_channel = extract_red(img)
    
    # Save the individual channels for visual inspection
    cv2.imwrite('southafrica_blue_channel.png', blue_channel)
    cv2.imwrite('southafrica_green_channel.png', green_channel)
    cv2.imwrite('southafrica_red_channel.png', red_channel)
    
    # Create a grayscale version for comparison
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('southafrica_grayscale.png', grayscale)
    
    # Calculate statistics for each channel
    print("\n=== CHANNEL STATISTICS ===")
    print(f"Blue channel - Min: {np.min(blue_channel)}, Max: {np.max(blue_channel)}, Mean: {np.mean(blue_channel):.2f}, Std: {np.std(blue_channel):.2f}")
    print(f"Green channel - Min: {np.min(green_channel)}, Max: {np.max(green_channel)}, Mean: {np.mean(green_channel):.2f}, Std: {np.std(green_channel):.2f}")
    print(f"Red channel - Min: {np.min(red_channel)}, Max: {np.max(red_channel)}, Mean: {np.mean(red_channel):.2f}, Std: {np.std(red_channel):.2f}")
    print(f"Grayscale - Min: {np.min(grayscale)}, Max: {np.max(grayscale)}, Mean: {np.mean(grayscale):.2f}, Std: {np.std(grayscale):.2f}")
    
    # Calculate correlation with grayscale
    blue_corr = np.corrcoef(blue_channel.flatten(), grayscale.flatten())[0, 1]
    green_corr = np.corrcoef(green_channel.flatten(), grayscale.flatten())[0, 1]
    red_corr = np.corrcoef(red_channel.flatten(), grayscale.flatten())[0, 1]
    
    print("\n=== CORRELATION WITH GRAYSCALE ===")
    print(f"Blue channel correlation: {blue_corr:.4f}")
    print(f"Green channel correlation: {green_corr:.4f}")
    print(f"Red channel correlation: {red_corr:.4f}")
    
    # Find which channel has highest correlation
    correlations = {'Blue': blue_corr, 'Green': green_corr, 'Red': red_corr}
    best_channel = max(correlations, key=correlations.get)
    
    print(f"\n=== CONCLUSION ===")
    print(f"The {best_channel} channel has the highest correlation with grayscale ({correlations[best_channel]:.4f})")
    
    return blue_channel, green_channel, red_channel, grayscale

if __name__ == "__main__":
    analyze_southafrica_channels()
