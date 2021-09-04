import React from "react";

class PriceTag extends React.Component {
    render() {
        return (
            <div>
                <span>{this.props.price.store}</span>
                <span>{this.props.price.price}</span>
                <span className={this.props.price.availalbe ? 'available' : 'unavailable'}>{this.props.price.available ? 'yes' : 'no'}</span>
            </div>
        );
    }
}

export default PriceTag