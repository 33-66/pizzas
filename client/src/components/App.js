import { Route ,Routes } from "react-router-dom";
import Restaurant from "./Home";
import Navbar from "./NavBar";
import Home from "./Restaurant";
// import {Switch} from  'react-router';

function App() {
  return (
    <>
      <Navbar />
    <Routes>
        
            <Route path="/" element={<Restaurant/>}></Route>
            <Route path="/restaurants/:id" element={<Home />}></Route>
            
        {/* </Route> */}
        
        </Routes>  
    
    </>
  );
}

export default App;
