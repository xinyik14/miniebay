import React from 'react';
import Actions from '../actions/actions';

class SearchBar extends React.Component {

  _handleChange(event) {
    Actions.filterProducts(event.target.value);
  }

  render() {
    const handleChange = this._handleChange.bind(this);
    return (
      <div className="row">
        <div className="col-md-8"></div>
        <div class="col-md-4">
        <input 
          type='text'
          onChange={handleChange}
          placeholder='Search...' />
        </div>
      </div>
    )
  }
}

export default SearchBar;
