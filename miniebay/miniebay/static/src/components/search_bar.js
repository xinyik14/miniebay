import React from 'react';
import Actions from '../actions/actions';

class SearchBar extends React.Component {

  _handleChange(event) {
    Actions.filterProducts(event.target.value);
  }

  render() {
    const handleChange = this._handleChange.bind(this);
    return (
      <div className="row" style={{position: "relative", top:"40px", bottom:"50px"}}>
        <div className="col-md-8"></div>
        <div class="col-md-4">
        <input 
          type='text'
          onChange={handleChange}
          placeholder='Search...' 
          aria-describedby="sizing-addon1" />
        </div>
      </div>
    )
  }
}

export default SearchBar;
