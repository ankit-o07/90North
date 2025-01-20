# Responsive Web Application with Dynamic Sidebar and Scaling

This project is a responsive web application with a dynamic sidebar and content scaling functionality. The application features a user-friendly layout and a modern design. The sidebar can be toggled open and closed, while the page adjusts its scaling dynamically based on the window size.

## Features

### 1. Dynamic Sidebar
- A collapsible left sidebar for navigation with smooth open and close animations.
- The sidebar contains a close button (`❌`) for better user experience.
- Sidebar items highlight and expand slightly on hover, giving visual feedback to the user.

### 2. Responsive Design
- The layout adjusts seamlessly to different screen sizes, ensuring usability across devices.
- Navigation links and settings are hidden on smaller screens to prioritize content visibility.
- A menu button (`☰`) is displayed on smaller screens for easier access to the sidebar.

### 3. Dynamic Page Scaling
- The `super` element adjusts its scale dynamically based on the screen width:
  - 0.9x for medium-large screens (992px to 1600px).
  - 0.8x for medium screens (700px to 767px).
  - 0.75x for smaller screens (600px to 700px).
  - 0.5x for very small screens (below 600px).
- Scaling ensures the UI elements fit well without breaking the layout.

### 4. Quick Links and Recent Activities Section
- A right sidebar contains "Quick Links" and "Recent Activities" for easy access to key features and updates.
- Both sections feature a clean, user-friendly design with hover effects.

## Technologies Used

### Frontend
- **HTML5**: Markup for structuring the layout.
- **CSS3**: Styling with modern features like variables, transitions, and responsive design.
- **JavaScript (Vanilla)**: Adding interactivity (sidebar toggle, dynamic scaling).

### Fonts & Icons
- Google Fonts: "Great Vibes" for stylish typography.
- Unicode icons for menu (`☰`) and close (`❌`) buttons.

## File Structure

```plaintext
/
├── index.html       # Main HTML file
├── style.css        # CSS file for styling
├── index.js         # JavaScript file for interactivity
└── README.md        # Project documentation
```

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/ankit-o07/90North.git

   ```
2. Navigate to the project directory:
   ```bash
   cd frontendDevelopmentTask
   ```
3. Open `index.html` in your browser to view the application:
   ```bash
   open index.html
   ```


## Future Enhancements
- **Add animations**: Enhance user experience by animating elements like list item expansion and page transitions.
- **Mobile-first design**: Further refine mobile usability with touch-friendly gestures.
- **User preferences**: Save sidebar state and scaling preferences using localStorage.



## Screenshots
screenshots of the application showcasing the sidebar, scaling, and responsiveness.

![alt text](<../Screenshot 2025-01-20 150341.png>)
![alt text](<../Screenshot 2025-01-20 150446.png>)