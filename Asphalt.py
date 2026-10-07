import math


class AsphaltEstimator:
    """Quantity takeoffs for asphalt paving materials."""

    def paving(
        self,
        area_sqft,
        thickness_inches,
        mix_density_lb_per_cuft=145,
        waste_percent=5
    ):
        """Estimate hot-mix asphalt tonnage from area and compacted depth."""
        if any(float(value) <= 0 for value in (
            area_sqft, thickness_inches, mix_density_lb_per_cuft
        )):
            raise ValueError(
                "Area, thickness, and mix density must be greater than zero."
            )
        if float(waste_percent) < 0:
            raise ValueError("Waste allowance cannot be negative.")

        volume_cuft = float(area_sqft) * float(thickness_inches) / 12
        base_tons = volume_cuft * float(mix_density_lb_per_cuft) / 2000
        order_tons = math.ceil(
            base_tons * (1 + float(waste_percent) / 100) * 10
        ) / 10

        return {
            "type": "Asphalt Paving",
            "material": "Hot-Mix Asphalt",
            "area_sqft": area_sqft,
            "thickness_inches": thickness_inches,
            "mix_density_lb_per_cuft": mix_density_lb_per_cuft,
            "volume_cuft": round(volume_cuft, 2),
            "estimated_tons": round(base_tons, 2),
            "waste_percent": waste_percent,
            "order_quantity": order_tons,
            "purchase_unit": "tons",
            "note": (
                "Planning quantity only. Confirm mix design, delivered density, "
                "compaction, lift thickness, and waste with the paving supplier "
                "and project specifications. This estimate excludes excavation, "
                "subbase, tack coat, and labor."
            )
        }
