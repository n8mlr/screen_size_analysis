# Screen Size Analysis Process

## Data Preparation

1. In Google Analytics, go to Custom Reports and Select "Browser Window Sizes and Device Category"
2. Set secondary dimension to 'Device Category'
3. Download entire dataset
4. Extract counts of screen sizes to screen_size_counts.csv
     1. Generate a flattened list of each instance, e.g. 1080x810,2 -> list this item twice
     2. Compute the area, w*h
     3. Compute an aspect ratio w/h



## What we want to find

* 95% of the most common browser widths
* 95% of the most common browser heights







## Findings

### Adam Fungent is unable to fully use our product due to usability issues

* Adam was unable to zoom into the map on his laptop because the browser window height hid the zoom controls
* 



### 20% of desktop users are missing the complete desktop experience

* When the browser window height goes below 600px, drawings become unusable as the drawing tool bar will overlap with the Zoom and Layer controls
* The app hides zoom controls when the user's browser window height is below 650px
* The zoom control is 96px tall. If added vertically the entire design would need to be at least 696px tall
* 



### Our system is functionally undesirable at browser heights below X





* Our system will become unusable at browser heights of 