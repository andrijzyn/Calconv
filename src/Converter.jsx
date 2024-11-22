import { useState } from 'react';
import PropTypes from 'prop-types';


const Converter = ({ onConvert }) => {
    const [number, setNumber] = useState('');
    const [fromBase, setFromBase] = useState(10);
    const [toBase, setToBase] = useState(10);

    const handleSubmit = (event) => {
        event.preventDefault();
        const expression = `${number}_${fromBase}to${toBase}`;
        onConvert(expression);
    };

    return (
        <div className="container converter-container">
            <h3>Converter</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Number:</label>
                    <input
                        type="text"
                        value={number}
                        onChange={(e) => setNumber(e.target.value)}
                        placeholder="Enter number (e.g., 101)"
                        required
                    />
                    <label>From Base:</label>
                    <input
                        type="number"
                        value={fromBase}
                        onChange={(e) => setFromBase(e.target.value)}
                        min="2"
                        max="36"
                        placeholder="Base"
                        required
                    />
                    <label>To Base:</label>
                    <input
                        type="number"
                        value={toBase}
                        onChange={(e) => setToBase(e.target.value)}
                        min="2"
                        max="36"
                        placeholder="Base"
                        required
                    />
                </div>
                <button type="submit">Convert</button>
            </form>
        </div>
    );
};

Converter.propTypes = {
    onConvert: PropTypes.func.isRequired, // must be a function and is required
};

export default Converter;