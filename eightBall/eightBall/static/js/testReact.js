//testReact.js
var DummyHTML = React.createClass({displayName: 'DummyHTML',
	render: function() {
		return(
			React.createElement('div', {className: 'butts'},
				"Hello, world!"
			)
		);
	}
});

ReactDOM.render(
	React.createElement(DummyHTML, null),
	document.getElementById('reactContent')
);