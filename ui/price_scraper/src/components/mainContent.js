import React from "react";
import ProductList from "./productList";

class MainContent extends React.Component {
    componentDidMount() {
        console.log("test create")
    }

    render() {
        return (
            <ProductList url={'http://localhost:8000/products/'} />
        );
    }

}

export default MainContent