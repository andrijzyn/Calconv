import { useState } from 'react';
import useRequest from './useRequest';

const Calculator = () => {
    const [num1, setNum1] = useState('');
    const [operator, setOperator] = useState('+');
    const [num2, setNum2] = useState('');
    const [base, setBase] = useState(10);

    const { result, steps, handleRequest } = useRequest();

    const handleSubmit = async (event) => {
        event.preventDefault();
        const url = 'http://localhost:5000/math';
        const data = {
            num1,
            num2,
            base,
            operator
        };

        await handleRequest(url, data);
    };

    console.log("Received steps:", steps);

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="num1">Number 1:</label>
                <input
                    type="text"
                    id="num1"
                    value={num1}
                    onChange={(e) => setNum1(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="num2">Number 2:</label>
                <input
                    type="text"
                    id="num2"
                    value={num2}
                    onChange={(e) => setNum2(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="base">Base:</label>
                <input
                    type="number"
                    id="base"
                    value={base}
                    onChange={(e) => setBase(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="operator">Operator:</label>
                <select
                    id="operator"
                    value={operator}
                    onChange={(e) => setOperator(e.target.value)}
                >
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">*</option>
                    <option value="/">/</option>
                </select>
            </div>

            <button type="submit">Calculate</button>

            {result && (
                <div>
                    <h3>Result:</h3>
                    <p>{result}</p>
                </div>
            )}

            {steps && steps.length > 0 && (
                <div>
                    <h3>Steps:</h3>
                    <ul> {steps} </ul>
                </div>
            )}
        </form>
    );
};

export default Calculator;