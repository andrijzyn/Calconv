import { useState } from 'react';
import PropTypes from 'prop-types';
import Converter from "./Converter.jsx";


const Calculator = ({ onCalculate }) => {
    const [num1, setNum1] = useState('');
    const [base1, setBase1] = useState(10);
    const [operator, setOperator] = useState('+');
    const [num2, setNum2] = useState('');
    const [base2, setBase2] = useState(10);

    const handleSubmit = (event) => {
        event.preventDefault();
        const expression = `${num1}_${base1} ${operator} ${num2}_${base2}`;
        onCalculate(expression);
    };

    return (
        <div className="container calculator-container">
            <h3>Calculator</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Number 1:</label>
                    <input type="text" value={num1} onChange={(e) => setNum1(e.target.value)} placeholder="Enter number (e.g., A5)" required />
                    <label>Base:</label>
                    <input type="number" value={base1} onChange={(e) => setBase1(e.target.value)} min="2" max="36" placeholder="Base" required />
                </div>
                <div>
                    <label>Operator:</label>
                    <select value={operator} onChange={(e) => setOperator(e.target.value)} required>
                        <option value="+">+</option>
                        <option value="-">-</option>
                        <option value="*">*</option>
                        <option value="/">/</option>
                    </select>
                </div>
                <div>
                    <label>Number 2:</label>
                    <input type="text" value={num2} onChange={(e) => setNum2(e.target.value)} placeholder="Enter number (e.g., 101)" required />
                    <label>Base:</label>
                    <input type="number" value={base2} onChange={(e) => setBase2(e.target.value)} min="2" max="36" placeholder="Base" required />
                </div>
                <button type="submit">Calculate</button>
            </form>
        </div>
    );
};

Calculator.propTypes = {
    onCalculate: PropTypes.func.isRequired, // must be a function and is required
};

export default Calculator;