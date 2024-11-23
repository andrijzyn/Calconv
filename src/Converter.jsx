import { useState } from 'react';
import useRequest from './useRequest';

const Converter = () => {
    const [number, setNumber] = useState('');
    const [fromBase, setFromBase] = useState(10);
    const [toBase, setToBase] = useState(10);

    const { result, steps, handleRequest } = useRequest();

    const handleSubmit = async (event) => {
        event.preventDefault();
        const url = 'http://localhost:5000/convert';
        const data = {
            number,
            fromBase,
            toBase
        };

        await handleRequest(url, data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="number">Number:</label>
                <input
                    type="text"
                    id="number"
                    value={number}
                    onChange={(e) => setNumber(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="fromBase">From Base:</label>
                <input
                    type="number"
                    id="fromBase"
                    value={fromBase}
                    onChange={(e) => setFromBase(e.target.value)}
                />
            </div>

            <div>
                <label htmlFor="toBase">To Base:</label>
                <input
                    type="number"
                    id="toBase"
                    value={toBase}
                    onChange={(e) => setToBase(e.target.value)}
                />
            </div>

            <button type="submit">Convert</button>

            {result && (
                <div>
                    <h3>Result:</h3>
                    <p>{result}</p>
                </div>
            )}

            {steps && steps.length > 0 && (
                <div>
                    <h3>Steps:</h3>
                    <ul>
                        {steps.map((step, index) => (
                            <li key={index}>{step}</li>
                        ))}
                    </ul>
                </div>
            )}
        </form>
    );
};

export default Converter;