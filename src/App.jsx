import { useState } from 'react';
import Calculator from './Calculator';
import Converter from './Converter';
import './App.css';

const App = () => {
    const [result, setResult] = useState('');
    const [steps, setSteps] = useState('');

    const handleRequest = async (url, expression) => {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ expression }),
            });
            const data = await response.json();
            return {
                result: data.result || data.error,
                steps: data.steps ? data.steps.join('\n') : 'No steps available',
            };
        } catch (error) {
            return { result: 'Error: ' + error.message, steps: '' };
        }
    };

    const handleCalculate = async (expression) => {
        const url = 'http://localhost:5000/process';
        const { result, steps } = await handleRequest(url, expression);
        setResult(result);
        setSteps(steps);
    };

    const handleConvert = async (expression) => {
        const url = 'http://localhost:5000/process';
        const { result, steps } = await handleRequest(url, expression);
        setResult(result);
        setSteps(steps);
    };

    return (
        <div className="app">
            <h2>Base Converter and Calculator</h2>
            <div id="flex-container">
                <Calculator onCalculate={handleCalculate} />
                <Converter onConvert={handleConvert} />
            </div>
            <hr />
            <h3>Steps:</h3>
            <pre id="steps">{steps}</pre>
            <h3>Result:</h3>
            <pre id="result">{result}</pre>
        </div>
    );
};

export default App;