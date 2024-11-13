url = 'http://localhost:5000/process';

const handleFormSubmission = async (event, url, expression) => {
    event.preventDefault();
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({expression})
        });
        const result = await response.json();
        document.getElementById('result').textContent = result.result || result.error;
        if (result.steps) {
            document.getElementById('steps').textContent = result.steps.join('\n');
        } else {
            document.getElementById('steps').textContent = 'No steps available';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: ' + error.message;
    }
};

document.getElementById('calculator-form').addEventListener('submit',
    (event) => {
        const num1 = document.getElementById('num1').value;
        const base1 = document.getElementById('base1').value;
        const operator = document.getElementById('operator').value;
        const num2 = document.getElementById('num2').value;
        const base2 = document.getElementById('base2').value;
        const expression = `${num1}_${base1} ${operator} ${num2}_${base2}`;
        handleFormSubmission(event, url, expression).catch(console.error);
    });

document.getElementById('conversion-form').addEventListener('submit',
    (event) => {
        const number = document.getElementById('convert-number').value;
        const base1 = document.getElementById('convert-base1').value;
        const base2 = document.getElementById('convert-base2').value;
        const expression = `${number}_${base1}to${base2}`;
        handleFormSubmission(event, url, expression).catch(console.error);
    });