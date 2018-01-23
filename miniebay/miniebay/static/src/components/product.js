class ProductRow extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      name: props.name,
      description: props.description,
      price: props.price
    };
  }

  render() {
    return (
      <tr>
        <td>{this.state.name}</td>
        <td>{this.state.price}</td>
        <td>{this.state.description}</td>
      </tr>
    );
  }
}

export default ProductRow;
