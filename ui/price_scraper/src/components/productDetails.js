import React from "react";
import PriceTag from "./priceTag";

class ProductDetails extends React.Component {
    render() {
        let prices_list;
        if (this.props.details.current_prices) {
                prices_list = this.props.details.current_prices.map((price) => <PriceTag key={price.slug} price={price}/>)
            }

        return (
            <div>
                <a href={this.props.details.url}><h1>{this.props.details.name}</h1></a>
                {prices_list}
                <p>{this.props.details.category}</p>
            </div>

        )

    }
}

export default ProductDetails