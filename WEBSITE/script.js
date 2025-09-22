document.addEventListener('DOMContentLoaded', () => {
    // --- Get references to HTML elements ---
    const quizForm = document.getElementById('quiz-form');
    const surveyContainer = document.getElementById('survey-container');
    const resultsContainer = document.getElementById('results-container');
    const retakeBtn = document.getElementById('retake-btn');

    // --- Listen for form submission ---
    quizForm.addEventListener('submit', (event) => {
        // Prevent the default form submission (which reloads the page)
        event.preventDefault();

        // --- 1. Validation: Check if all 12 questions are answered ---
        const checkedRadios = document.querySelectorAll('input[type="radio"]:checked');
        if (checkedRadios.length < 12) {
            alert("Please answer all 12 questions before proceeding.");
            return; // Stop the function here
        }

        // --- 2. Scoring Logic ---
        let totalScore = 0;
        checkedRadios.forEach(radio => {
            // Add the integer value of the selected radio button to the score
            totalScore += parseInt(radio.value, 10);
        });

        // --- 3. Display Results ---
        displayResult(totalScore);
    });

    // --- Function to show the correct result page ---
    function displayResult(score) {
        // Hide the survey form
        surveyContainer.classList.add('hidden');
        
        // Hide all result pages first to ensure a clean slate
        document.querySelectorAll('.result-page').forEach(page => page.classList.add('hidden'));

        // Show the correct result page based on the new score ranges
        if (score <= 7) { // Low Risk
            document.getElementById('low-risk-result').classList.remove('hidden');
        } else if (score <= 16) { // Medium Risk
            document.getElementById('medium-risk-result').classList.remove('hidden');
        } else { // High Risk (17+)
            document.getElementById('high-risk-result').classList.remove('hidden');
        }

        // Show the main results container
        resultsContainer.classList.remove('hidden');
    }

    // --- Listen for the "Retake Survey" button click ---
    retakeBtn.addEventListener('click', () => {
        // Hide the results
        resultsContainer.classList.add('hidden');
        
        // Show the survey
        surveyContainer.classList.remove('hidden');

        // Reset the form to clear all selections
        quizForm.reset();

        // Scroll to the top of the page for a better user experience
        window.scrollTo(0, 0);
    });
});