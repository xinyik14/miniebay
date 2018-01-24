import React from 'react';
import ReactDOM from 'react-dom';
import ProductTable from './components/product_table.js';
import ProductNew from './components/product_new.js';
import SearchBar from './components/search_bar.js';

class Main extends React.Component {
  render() {
    return ( 
      <div>
        <div class="page-header">
           <h1 style={{color:"#002080", textAlign:"center",position:"relative", top:"20px", bottom:"30px"}}>Mini Ebay <small>product listing web</small></h1>
        </div>
        <SearchBar />
        <ProductTable />
        <ProductNew />
      </div>
    );
  }
}
ReactDOM.render(
  <Main/>,
  document.getElementById('app')
);
