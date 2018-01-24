import React from 'react';
import API from '../utils/api';

class ProductNew extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      name: '',
      // TODO: hard code to user_id 1 for now before login is finished
      user_id: 1,
      price: 0,
      description: '',
      error: ''
    };
  }

  _handleNameChange(event) {
    this.setState({name: event.target.value});
  }

  _handlePriceChange(event) {
    this.setState({price: event.target.value});
  }

  _handleDescriptionChange(event) {
    this.setState({description: event.target.value});
  }

  _handleSubmit(event) {
    event.preventDefault();
    const {name, price, description, user_id} = this.state;
    if (name === '') {
      this.setState({error: 'no name specified'});
      return;
    }
    this.setState({error: ''});
    API.createProduct({
      name,
      price,
      description,
      user_id,
    }, API.getProducts);
  }

  render() {
    const {name, price, description, error} = this.state;
    const handleNameChange = this._handleNameChange.bind(this);
    const handlePriceChange = this._handlePriceChange.bind(this);
    const handleDescriptionChange = this._handleDescriptionChange.bind(this);
    return (
      <div style={{position: "relative", left:"30px", top:"80px"}}>
        <h3>Create New Product</h3>
        <form onSubmit={this._handleSubmit.bind(this)}>
          <span>
            <label htmlFor='name'>Name:</label>
            <input id='name' name='name' type='text' value={name} onChange={handleNameChange}></input>
          </span><br/>
          <span>
            <label htmlFor='price'>Price:</label>
            <input id='price' name='price' type='text' value={price} onChange={handlePriceChange}></input>
          </span><br/>
          <span>
            <label htmlFor='desc'>Description:</label><br/>
            <textarea id='desc' name='description' value={description} onChange={handleDescriptionChange}></textarea>
          </span><br/>
          <input type='submit'></input>
        </form>
        <span><p style={{color:"red"}}>{error}</p></span>
      </div>
    );
  }
}

export default ProductNew;
