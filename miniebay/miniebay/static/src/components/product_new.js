import React from 'react';

class ProductNew extends React.Component {

  render() {
    return (
      <div>
        <h3>Create New Product</h3>
        <form>
          <span>
            <label for='name'>Name:</label>
            <input id='name' name='name' type='text'></input>
          </span><br/>
          <span>
            <label for='price'>Price:</label>
            <input id='price' name='price' type='text'></input>
          </span><br/>
          <span>
            <label for='desc'>Description:</label><br/>
            <textarea id='desc' name='description'></textarea>
          </span><br/>
          <input type='submit'></input>
        </form>
      </div>
    );
  }
}

export default ProductNew;
