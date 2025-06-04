# FUTURE FEATURES ROADMAP

Below is a list of features and improvements planned for future versions of this health‐tracker application. Keeping an explicit roadmap helps demonstrate to recruiters and collaborators that you can plan ahead and iterate over time.

---

## Stat Tracker (stat_tracker.py)
1. **Export/Import to CSV**  
   - TODO: Add option to export `stat_data.json` to a CSV file (e.g., `stats_export.csv`) for use in Excel or Google Sheets.  
   - TODO: Allow user to import a CSV of previous entries (for migration).

2. **Interactive Charts & Visualizations**  
   - TODO: Generate a simple line chart of weight vs. date (e.g., using `matplotlib` or `plotly`).  
   - TODO: Visualize weekly or monthly averages of BMI or body fat.

3. **User Profiles & Authentication**  
   - TODO: Expand from a single-user CLI to a multi-user system (username + password).  
   - TODO: Encrypt JSON files with a simple symmetric key to protect user data.

4. **TDEE Estimation & Macro Recommendations**  
   - TODO: Implement the Mifflin–St Jeor and/or Katch–McArdle formulas in `calculate_tdee(...)`.  
   - TODO: After adding a stat entry, automatically show recommended calories and macro breakdown for bulk/cut/maintain.  
   - TODO: Allow user to specify goal (“bulk”, “cut”, “maintain”) and return a suggested daily calorie intake.

5. **Profile Picture / Avatar Support**  
   - TODO: Let users assign a local image (or choose from pre‐built avatars) to their profile.  
   - TODO: Store image references in JSON so that a future GUI can display them.

6. **Cloud Sync / Mobile App Integration**  
   - TODO: Sync JSON data to a remote (Firebase, AWS S3) so stats persist across devices.  
   - TODO: Build a simple mobile app (React Native or Flutter) that reads/writes to the same backend JSON, enabling on‐the‐go logging.

---

## Food Inventory (food_inventory.py)
1. **Nutritional Database Integration**  
   - TODO: Implement `fetch_nutritional_info(food_name)` using the USDA FoodData Central API or a similar public API, so users can simply type “banana” and have calories/macros auto‐populate.  
   - TODO: Cache API responses locally (in a separate JSON “food_cache.json”) to reduce repeated API calls.

2. **Category & Tagging**  
   - TODO: Let users tag food items (e.g., “protein”, “fats”, “snack”) and filter by tags.  
   - TODO: Implement a “favorite foods” list for quick data entry.

3. **Create/Read/Update/Delete (CRUD) GUI**  
   - TODO: Build a basic web frontend using Flask + Jinja2 to display food inventory in a table, allow inline editing, and show item details in a modal.  
   - TODO: Add image uploads (sprite icons) for each food item, displayed next to the name in the table.

4. **Recipe Builder & Meal Logging**  
   - TODO: Allow users to combine multiple food items into a “recipe” or “meal,” automatically summing macros and calories.  
   - TODO: Store meal logs with date/time stamps so users can see “Breakfast”, “Lunch”, “Dinner” separate entries.

---

## UX/UI / Interface Design 
1. **Wireframes & Mockups**  
   - TODO: Create initial wireframes in Figma or Adobe XD to sketch how web pages will look.  
   - TODO: Design a “dashboard” landing page where users see a summary of stats (e.g., “Weight Trend Chart,” “Today’s Calories,” “Goal Progress”).

2. **Responsive Web Design**  
   - TODO: Use a CSS framework (Bootstrap, Tailwind, or custom) to ensure mobile responsiveness.  
   - TODO: Test on small screens so the menus and forms scale appropriately.

3. **Gamification Elements**  
   - TODO: Add “streak” counter (e.g., “You’ve logged your stats 5 days in a row”) and display badges or progress bars.  
   - TODO: Incorporate subtle animations (e.g., confetti when a user hits a milestone).

4. **Accessibility & Internationalization**  
   - TODO: Ensure keyboard navigation works (using `tabindex`, `aria-label`).  
   - TODO: Add support for metric vs. imperial units (kg vs. lbs, cm vs. inches).  
   - TODO: Provide translations (e.g., Spanish, French) for all prompts and labels.

---

## General Project Management
1. **Add Unit Tests**  
   - TODO: Write `pytest` or `unittest` tests covering input validation, JSON read/write, and calculation logic.  
   - TODO: Set up a GitHub Actions workflow to run tests on every push.

2. **Continuous Integration (CI) / Continuous Deployment (CD)**  
   - TODO: Configure GitHub Actions to lint Python code (flake8 or black), run tests, and deploy updates to a staging server.  
   - TODO: Automate deployment of a static front end (HTML/CSS/JS) to GitHub Pages whenever the `main` branch changes.

3. **Documentation & Code Comments**  
   - TODO: Expand docstrings on every function to explain parameters, return types, and side effects.  
   - TODO: Create a dedicated `docs/` folder with markdown-based documentation on code architecture, data schema, and API endpoints (for a future web service).

4. **Versioning & Release Notes**  
   - TODO: Tag releases in Git (e.g., `v1.0.0`) when major features land.  
   - TODO: Maintain a `CHANGELOG.md` listing new features, bug fixes, and version increments.

---

_End of roadmap. Update this file as you complete items or add new ones._  
