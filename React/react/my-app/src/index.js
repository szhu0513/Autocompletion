import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Autocompletion extends React.Component{
	constructor(props){
		super(props)
		this.queryWord=React.createRef()
		this.state={
			query:"",
			results: [],
		}
	}
	renderResults(){
		var resultList = []
		for(var result of this.state.results){
			resultList.push(<li key={result}>{result}</li>)
		}
		return resultList
	}
	query(){
	        fetch("/query?q="+this.state.query)
		.then(res =>res.json())
		.then((result)=>{
			var autocompletions = ["NOTHING FOUND!"]
			if (result["autocompletion"].length!==0) {
				autocompletions = result["autocompletion"]
			}
			this.setState({
				results: autocompletions,
			})
		},
			(error)=>{
				console.log("request error:" +error)
			}
		)


	}
	render() {
           return (
		    <div>
		    <h1>AUTOCOMPLETION</h1>
		    <h2>{process.env.HOST_IP}</h2>
		    <input type="text" name="query" onChange={
			    (e)=> {
				    this.setState({
					    query:e.target.value
				    })
			    }
		    }/>
	   	    <button onClick={()=>this.query()}>search</button>
		    <ul>{this.renderResults()}</ul>
		    </div>
  		  );
 	 }

}


// ========================================

ReactDOM.render(
  <Autocompletion />,
  document.getElementById('root')
);
