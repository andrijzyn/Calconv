import { useState } from 'react';
import Calculator from './Calculator';
import Converter from './Converter';
import Steps from './Steps';
import Result from './Result';
import './App.css';
import useRequest from './useRequest';

const App = () => {
    const { result, steps, handleRequest } = useRequest();

    const handleCalculate = async (expression) => {
        const url = 'http://localhost:5000/process';
        await handleRequest(url, expression);
    };

    const handleConvert = async (expression) => {
        const url = 'http://localhost:5000/process';
        await handleRequest(url, expression);
    };

    return (
        <div className="app">
            <h2>Base Converter and Calculator</h2>
            <div id="flex-container">
                <Calculator onCalculate={handleCalculate} />
                <Converter onConvert={handleConvert} />
            </div>
            <hr />
            <Steps steps={steps} />
            <Result result={result} />
        </div>
    );
};

export default App;
