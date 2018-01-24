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
      <table className="table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    );
  }
}

export default ProductTable;
