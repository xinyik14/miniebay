import React from 'react';
import Actions from '../actions/actions';

class SearchBar extends React.Component {

  _handleChange(event) {
    Actions.filterProducts(event.target.value);
  }

  render() {
    const handleChange = this._handleChange.bind(this);
    return (
      <form>
        <input 
          type='text' 
          onChange={handleChange}
          placeholder='Search...' />
      </form>
    )
  }
}

export default SearchBar;
