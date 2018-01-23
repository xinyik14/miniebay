import React from 'react';
class ProductRow extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const name = this.props.name;
    const price = this.props.price;
    const description = this.props.description;
    return (
      <tr>
        <td>{name}</td>
        <td>{price}</td>
        <td>{description}</td>
      </tr>
    );
  }
}

export default ProductRow;
