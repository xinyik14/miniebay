import React from 'react';
import ReactDOM from 'react-dom';
import ProductTable from './components/product_table.js';

class Main extends React.Component {
  render() {
    return ( 
      <p>Hello world</p>
    );
  }
}
ReactDOM.render(
  <Main/>,
  document.getElementById('app')
);
