import { useState } from 'react';

const useRequest = () => {
    const [result, setResult] = useState('');
    const [steps, setSteps] = useState([]);

    const handleRequest = async (url, data) => {
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
            console.error('Error during the request:', error);
        }
    };

    return {
        result,
        steps,
        handleRequest,
    };
};

export default useRequest;
