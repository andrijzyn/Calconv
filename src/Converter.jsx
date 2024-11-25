import { useState } from 'react';
import useRequest from './useRequest';
import { JSONTree } from 'react-json-tree';

const Converter = () => {
    const [number, setNumber] = useState('');
    const [fromBase, setFromBase] = useState(10);
    const [toBase, setToBase] = useState(10);

    const { result, steps, error, handleRequest } = useRequest();

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
            <div className="text">
                <label htmlFor="number">Number:</label>
                <input
                    type="text"
                    id="number"
                    value={number}
                    onChange={(e) => setNumber(e.target.value)}
                />
            </div>
            <div className="input-row">
                <div className="input-group">
                    <label htmlFor="fromBase">From Base:</label>
                    <input
                        type="number"
                        id="fromBase"
                        value={fromBase}
                        onChange={(e) => setFromBase(e.target.value)}
                    />
                </div>

                <div className="input-group">
                    <label htmlFor="toBase">To Base:</label>
                    <input
                        type="number"
                        id="toBase"
                        value={toBase}
                        onChange={(e) => setToBase(e.target.value)}
                    />
                </div>
            </div>

            <button type="submit">Convert</button>

            {error && (
                <div style={{ color: 'red', marginTop: '10px' }}>
                    <strong>Error:</strong> {error.message}
                </div>
            )}

            <h3>Result:</h3>
            <div style={{ whiteSpace: 'pre-wrap', wordWrap: 'break-word' }}>
                <JSONTree data={result} />
            </div>

            <h3>Steps:</h3>
            <div style={{
                whiteSpace: 'pre-wrap',
                wordWrap: 'break-word'
            }}>
                <JSONTree data={steps}/>
            </div>
        </form>
    );
};

export default Converter;
