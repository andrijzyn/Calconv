import Calculator from './Calculator';
import Converter from './Converter';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css'

const App = () => {
  return (
    <div id="main-container" className="container-fluid d-flex vh-100">
      <div className="row flex-grow-1">
        <div className="col-md-6 d-flex align-items-center justify-content-center">
          <div className="card shadow-sm window p-4">
            <h3 className="card-title text-center" >Calculator</h3>
            <Calculator />
          </div>
        </div>
        <div className="col-md-6 d-flex align-items-center justify-content-center">
          <div className="card shadow-sm window p-4">
            <h3 className="card-title text-center">Converter</h3>
            <Converter />
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;