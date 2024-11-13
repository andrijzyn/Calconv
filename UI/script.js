document.getElementById('calculator-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const num1 = document.getElementById('num1').value;
    const base1 = document.getElementById('base1').value;
    const operator = document.getElementById('operator').value;
    const num2 = document.getElementById('num2').value;
    const base2 = document.getElementById('base2').value;
    const expression = `${num1}_${base1} ${operator} ${num2}_${base2}`;
    try {
        const response = await fetch('http://127.0.0.1:5000/process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ expression })
        });
        const result = await response.json();
        document.getElementById('result').textContent = result.result || result.error;
        if(result.steps) {
            document.getElementById('steps').textContent = result.steps.join('\n');
        } else {
            document.getElementById('steps').textContent = 'No steps available';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: ' + error.message;
    }
});

document.getElementById('conversion-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const number = document.getElementById('convert-number').value;
    const base1 = document.getElementById('convert-base1').value;
    const base2 = document.getElementById('convert-base2').value;
    const expression = `${number}_${base1}to${base2}`;
    try {
        const response = await fetch('http://localhost:5000/process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ expression })
        });
        const result = await response.json();
        document.getElementById('result').textContent = result.result || result.error;
        if(result.steps) {
            document.getElementById('steps').textContent = result.steps.join('\n');
        } else {
            document.getElementById('steps').textContent = 'No steps available';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: ' + error.message;
    }
});