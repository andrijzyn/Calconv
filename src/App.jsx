import Calculator from './Calculator';
import Converter from './Converter';
import './index.css';

const App = () => {
    return (
        <div className="app">
            <h2>Base Converter and Calculator</h2>
            <div id="flex-container">
                <Calculator />
                <Converter />
            </div>
        </div>
    );
};

export default App;