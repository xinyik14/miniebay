import ProductRow from './product.js';

class ProductTable extends React.Component {

  render() {
    const rows = this.props.products.map((product) => {
      <Product 
        name={product.name}
        price={product.price}
        description={product.description}/>
    });

    return (
      <table>
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
