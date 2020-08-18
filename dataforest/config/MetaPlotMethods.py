from dataforest.config.MetaConfig import MetaConfig
from dataforest.utils.loaders.collectors import collect_plots
from dataforest.utils.plots_config import parse_plot_methods, parse_plot_kwargs


class MetaPlotMethods(MetaConfig):
    @property
    def PLOT_METHOD_LOOKUP(cls):
        return {k: v for source in cls.CONFIG["plot_sources"] for k, v in collect_plots(source).items()}

    @property
    def PLOT_METHODS(cls):
        try:
            plot_methods = cls.CONFIG["plot_methods"]
        except KeyError:
            plot_methods = parse_plot_methods(config=cls.CONFIG)

        return plot_methods

    @property
    def PLOT_KWARGS_DEFAULTS(cls):
        return cls.CONFIG["plot_kwargs_defaults"]

    @property
    def PLOT_KWARGS(cls):  # TODO-QC: mapping of process, plot to kwargs
        plot_kwargs = parse_plot_kwargs(config=cls.CONFIG)

        return plot_kwargs