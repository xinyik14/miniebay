import React from 'react';
import ProductRow from './product_row.js';
import ProductStore from '../stores/product_store.js'
import API from '../utils/api';

class ProductTable extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      products: ProductStore.getState()
    };
  }

  componentWillMount() {
    API.getProducts();
  }

  // Listen for changes
  componentDidMount() {
    ProductStore.addChangeListener(() => this._onChange());
  }

  componentWillUnmount() {
    ProductStore.removeChangeListener(() => this._onChange());
  }

  _onChange() {
    this.setState({
      products: ProductStore.getState() 
    });
  }

  render() {
    const rows = [];
    this.state.products.forEach((product) => {
      rows.push(<ProductRow 
        key={product.id}
        name={product.name}
        price={product.price}
        description={product.description}/>
      );
    });

    return (
      <div className="panel panel-default" style={{position:"relative", top:"60px"}}>
        <div className="panel-heading" style={{color:"#1a53ff", fontSize: "20px"}}>Listing of products</div>
        <table className="table" style={{border: "groove", backgroundColor:"#f5f5f5"}}>
          <thead>
            <tr>
              <th>Name</th>
              <th>Price</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    );
  }
}

export default ProductTable;
