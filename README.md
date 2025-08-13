# Café Directory
A simple Flask web app for adding and viewing your favorite cafés. Users can submit details like location, opening hours, and ratings for coffee, Wi-Fi, and power outlets. All entries are stored in a CSV file and displayed instantly in the "View Cafes" page.

## Features
- Add new café details through a simple form.
- View all submitted cafés in a clean, table-like format.
- Data persistence using CSV — no database required.
- Form validation (ensures URLs and required fields are correct).
- Bootstrap styling for responsive UI.

## How It Works
- Home Page – Contains navigation to “Add a Café” or “View Cafes.”
- Add a Café – User fills out the form with:

### Café name

### Location (URL to Google Maps)

### Opening & closing times

### Ratings for coffee, Wi-Fi, and power outlets

### On Submit – Data is validated, saved to cafe-data.csv, and the user is redirected to the updated cafés list.

### View Cafes – Reads from cafe-data.csv and displays all entries in a table.

## Testing the App
- Start the server (python main.py).
- Go to Add a Café and submit a valid form (make sure the Location field is a valid URL like https://goo.gl/maps/...).
- After submission, you should be redirected to the cafés list and see your new entry at the bottom.
- Refresh the page to confirm data persists.

## Created By
Faiz

## AI Assistance
Claude.ai – Initial development guidance and suggestions.

ChatGPT – Debugging, logic fixes, and bug spotting.

# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
