import { useState } from 'react';

const useRequest = () => {
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
            setResult(data.result || data.error);
            setSteps(data.steps ? data.steps.join('\n') : 'No steps available');
        } catch (error) {
            setResult('Error: ' + error.message);
            setSteps('');
        }
    };

    return {
        result,
        steps,
        handleRequest
    };
};

export default useRequest;
