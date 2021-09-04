import React from "react";
import PriceTag from "./priceTag";
import Thumbnail from "./thumbnail";

class ProductDetails extends React.Component {
    render() {
        let prices_list;
        if (this.props.item.current_prices) {
                prices_list = this.props.name.current_prices.map((price) => <PriceTag price=price/>)
            }

        return (
            <div>
                <Thumbnail image_url=this.props.item.image_url/>
                <a href={this.props.item.url}><h1>{this.props.item.name}</h1></a>
                {prices_list}
            </div>

        )

    }
}