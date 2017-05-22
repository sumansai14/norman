import React from 'react';
import $ from 'jquery';

import ApiMixin from '../mixins/apiMixin';
import LoadingIndicator from '../components/loadingIndicator';

const App = React.createClass({
  childContextTypes: {
    location: React.PropTypes.object
  },

  mixins: [ApiMixin],

  getInitialState() {
    return {
      loading: false,
      error: false,
    };
  },
  getChildContext() {
    return {
      location: this.props.location
    };
  }

  render(){
    if (this.state.loading) {
      return (
        <LoadingIndicator triangle={true}>
          {t('Getting a list of all of your organizations.')}
        </LoadingIndicator>
      );
    }
  }
});

export default App;