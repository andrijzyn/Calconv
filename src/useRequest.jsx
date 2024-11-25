import { useState } from 'react';

const useRequest = () => {
    const [result, setResult] = useState('');
    const [steps, setSteps] = useState([]);
    const [error, setError] = useState(null);

    const handleRequest = async (url, data) => {
        setError(null);
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const responseData = await response.json();

            setResult(responseData.result);
            setSteps(responseData.steps);

        } catch (error) {
            const customError = {
                message: 'Request failed',
                code: 'SERVER_ERROR',
                details: error.message,
            };
            setError(customError);
        }
    };

    return {
        result,
        steps,
        error,
        handleRequest,
    };
};

export default useRequest;
